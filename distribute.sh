rm -rf build
rm -rf dist
rm -rf notion_database_bot.egg-info

python setup.py sdist bdist_wheel

twine upload dist/*