package survivedpassengers;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.*;

public class SurvivedPassengersMap extends MapReduceBase implements Mapper <LongWritable, Text, IntWritable, Text> {


	public void map(LongWritable key, Text value, OutputCollector <IntWritable, Text> output, Reporter reporter) throws IOException {

		String valueString = value.toString();
		String[] singlePassengerData = valueString.split(",");

		String status = "dead";
		int survived = Integer.parseInt(singlePassengerData[1]);

		if (survived == 1)
			status = singlePassengerData[4];

		output.collect(new IntWritable(Integer.parseInt(singlePassengerData[2])), new Text(status));
	}
}

