#!/bin/bash
input=
output=
#hadoop fs -rmr -skipTrash $output

hadoop jar /opt/cloudera/parcels/CDH/jars/hadoop-streaming-2.6.0-cdh5.5.0.jar \
	-files mapper.sh,mapper.py,protobuf.env,py/log_event_pb2.py \
	-archives hdfs://purple/user/sunshangchun/exchange/lib.tar.gz#lib \
	-io rawbytes \
	-cmdenv PYTHONPATH=lib:.:\$PYTHONPATH \
	-input $input \
	-inputformat org.apache.hadoop.mapred.SequenceFileInputFormat \
	-outputformat org.apache.hadoop.mapred.TextOutputFormat \
	-output $output \
	-numReduceTasks 0 \
	-mapper "python mapper.py"
	#-mapper "export PYTHONPATH=lib:.:\$PYTHONPATH && python mapper.py"
    #,typedbytes/typedbytes.py
	#-io typedbytes \
	#-io rawtypes \
	#-D mapred.reduce.tasks=0 \
