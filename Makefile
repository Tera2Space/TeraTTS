git:
	git add .
	git commit -m "update"
	git push -u -f origin main

pypi:
	rm -r ./build
	rm -r ./dist
	rm -r RUTTS.egg-info
	python setup.py sdist bdist_wheel
	twine upload dist/*