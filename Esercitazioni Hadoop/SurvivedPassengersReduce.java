package SurvivedPassengers;

import java.io.IOException;
import java.util.*;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.*;

public class SurvivedPassengersReduce extends MapReduceBase implements Reducer<IntWritable, Text, IntWritable, ArrayWritable> {

	public void reduce(IntWritable pclass, Iterator<Text> values, OutputCollector<IntWritable,ArrayWritable> output, Reporter reporter) throws IOException {

		float embarked = 0.0, survivedFemales = 0.0, survivedMales = 0.0;

		IntWritable passengersClass = pclass;


		while (values.hasNext()) {

			String value = ((Text)values.next()).toString();
			embarked += 1;
			
			if (value.equals("male"))
				survivedMales += 1;
			else if (value.equals("female"))
				survivedFemales += 1;
			
		}

		survivedMales /= embarked;
		survivedFemales /= embarked;

		output.collect(passengersClass, new ArrayWritable(FloatWritable, 
					{new FloatWritable(survivedMales),new FloatWritable(survivedFemales)}));
	}
}
