package SurvivedPassengers;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.*;

public class SurvivedPassengersMap extends MapReduceBase implements Mapper <LongWritable, Text, IntWritable, Text> {


	public void map(LongWritable key, Text value, OutputCollector <IntWritable, Text> output, Reporter reporter) throws IOException {

		String valueString = value.toString();
		String[] SinglePassengerData = valueString.split(",");

		String status = new String("dead");
		int survived = Integer.parseInt(SinglePassengerData[1]);

		if (survived == 1)
			status = SinglePassengerData[4]

		output.collect(new IntWritable(Integer.parseInt(SinglePassengerData[2])), new Text(status));
	}
}

