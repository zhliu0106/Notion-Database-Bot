rm -rf build
rm -rf dist
rm -rf notion-database-bot.egg-info

python setup.py sdist bdist_wheel

twine upload dist/*