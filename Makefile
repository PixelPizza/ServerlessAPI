build-UsersFunction:
	cp -a app $(ARTIFACTS_DIR)
	pip install -r app/requirements.txt -t $(ARTIFACTS_DIR)
	rm -rf $(ARTIFACTS_DIR)/bin
