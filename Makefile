test:
	@echo "run test"
	python3 test_dialog.py

release: release.sh
	@echo "create release"
	./release.sh

install:
	@echo "Plugin Directory"
	mkdir fanout-tool
	cp __init__.py fanout-tool/
	cp -r onekiwi/ fanout-tool/
	rm -rf ~/.local/share/kicad/6.0/scripting/plugins/fanout-tool/
	mv fanout-tool/ ~/.local/share/kicad/6.0/scripting/plugins
