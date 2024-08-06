import scipy.io.wavfile
import os
import sounddevice as sd
import onnxruntime
import numpy as np
from huggingface_hub import snapshot_download
from num2words import num2words
import re
from transliterate import translit
from .tokenizer import TokenizerG2P

class TTS:
    def __init__(self, model_name: str, save_path: str = "./model", add_time_to_end: float = 1.0, preprocess_nums=True, preprocess_trans=True, tokenizer_load_dict=True) -> None:
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        
        model_dir = os.path.join(save_path, model_name)
        
        if not os.path.exists(model_dir):
            snapshot_download(repo_id=model_name, 
                              allow_patterns=["*.txt", "*.onnx", "*.json"], 
                              local_dir=model_dir,
                              local_dir_use_symlinks=False
                            )
        
        self.model = onnxruntime.InferenceSession(os.path.join(model_dir, "exported/model.onnx"), providers=['CPUExecutionProvider'])
        self.preprocess_nums = preprocess_nums
        self.preprocess_trans = preprocess_trans
        
        self.tokenizer = TokenizerG2P(os.path.join(model_dir, "exported"), load_dict=tokenizer_load_dict)    
        
        self.add_time_to_end = add_time_to_end

    
    def _add_silent(self, audio, silence_duration: float = 1.0, sample_rate: int = 22050):
        num_samples_silence = int(sample_rate * silence_duration)
        silence_array = np.zeros(num_samples_silence, dtype=np.float32)
        audio_with_silence = np.concatenate((audio, silence_array), axis=0)
        return audio_with_silence


    def save_wav(self, audio, path:str):
        '''save audio to wav'''
        scipy.io.wavfile.write(path, 22050, audio)
    
    
    def play_audio(self, audio):
        sd.play(audio, 22050, blocking=True)
    
    
    def _intersperse(self, lst, item):
        result = [item] * (len(lst) * 2 + 1)
        result[1::2] = lst
        return result
    
    
    def _get_seq(self, text):
        phoneme_ids = self.tokenizer._get_seq(text)
        phoneme_ids_inter = self._intersperse(phoneme_ids, 0)
        return phoneme_ids_inter
        
    def _num2wordsshor(self, match):
        match = match.group()
        ret = num2words(match, lang ='ru')
        return ret 
    
    def __call__(self, text: str, play = False, length_scale=1.2):
        if self.preprocess_trans:
            text = translit(text, 'ru')
        
        if self.preprocess_nums:
            text = re.sub(r'\d+',self._num2wordsshor,text)
        phoneme_ids = self._get_seq(text)
        text = np.expand_dims(np.array(phoneme_ids, dtype=np.int64), 0)
        text_lengths = np.array([text.shape[1]], dtype=np.int64)
        scales = np.array(
            [0.667, length_scale, 0.8],
            dtype=np.float32,
        )
        audio = self.model.run(
            None,
            {
                "input": text,
                "input_lengths": text_lengths,
                "scales": scales,
                "sid": None,
            },
        )[0][0,0][0]
        audio = self._add_silent(audio, silence_duration = self.add_time_to_end)
        if play:
            self.play_audio(audio)
        return audio
