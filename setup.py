from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows',
  'Operating System :: Unix',
  'Operating System :: MacOS',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='RUTTS',
  version='0.1.7',
  description='russian text to speech',
  url='https://github.com/Tera2Space/RUTTS',  
  author='Tera Space',
  author_email='tera2space@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='tts', 
  packages=find_packages(),
  install_requires=['scipy', 'gruut', 'gruut-lang-ru', 'sounddevice', 'onnxruntime', 'huggingface-hub', "tok"] 
)