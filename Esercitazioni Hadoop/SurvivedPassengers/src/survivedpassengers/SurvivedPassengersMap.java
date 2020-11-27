package survivedpassengers;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.*;

public class SurvivedPassengersMap extends MapReduceBase implements Mapper <LongWritable, Text, IntWritable, Text> {


	public void map(LongWritable key, Text value, OutputCollector <IntWritable, Text> output, Reporter reporter) throws IOException {

		String passengerRecord = Text.decode(value.copyBytes());

		String[] passengerData = passengerRecord.split(",");

		String status = "";

		int survived = Integer.parseInt(passengerData[1]);

		if (passengerRecord.indexOf(",male,") > -1) 
				status = "male," + (survived == 1 ? "survived" : "dead");
		else if (passengerRecord.indexOf(",female,") > -1) 
				status="female," + (survived == 1 ? "survived" : "dead");

		output.collect(new IntWritable(Integer.parseInt(passengerData[2])), new Text(status));
	}
}

