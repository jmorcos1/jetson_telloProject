#!/bin/bash
/home/ece498/.local/bin/jupyter lab --allow-root \
	--ip 0.0.0.0 \
	--port 8889 \
	--ServerApp.password='' \
	--ServerApp.iopub_data_rate_limit=1.0e10 \
	--ContentsManager.allow_hidden=True
