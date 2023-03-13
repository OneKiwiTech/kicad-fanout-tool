test:
	@echo "Run test"
	python3 dialog.py

release: release.sh
	@echo "Create release"
	./release.sh

install:
	@echo "Install Plugin"
	mkdir fanout-tool
	cp __init__.py fanout-tool/
	cp -r onekiwi/ fanout-tool/
	rm -rf ~/.local/share/kicad/7.0/scripting/plugins/fanout-tool/
	mv fanout-tool/ ~/.local/share/kicad/7.0/scripting/plugins

uninstall:
	@echo "Uninstall Plugin"
	rm -rf ~/.local/share/kicad/7.0/scripting/plugins/fanout-tool/