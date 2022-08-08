test:
	@echo "run test"
	python3 test_dialog.py

release: release.sh
	@echo "create release"
	./release.sh