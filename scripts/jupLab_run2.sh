#!/bin/bash
/home/.local/bin/jupyter lab --allow-root \
	--ip 0.0.0.0 \
	--port 8887 \
	--ServerApp.password='' \
	--ServerApp.iopub_data_rate_limit=1.0e10 \
	--ContentsManager.allow_hidden=True
#run this from container!