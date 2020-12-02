package survivedpassengers;

import java.io.IOException;
import java.util.*;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.*;

public class SurvivedPassengersReduce extends MapReduceBase implements Reducer<IntWritable, Text, IntWritable, Text> {

	public void reduce(IntWritable pclass, Iterator<Text> values, OutputCollector<IntWritable,Text> output, Reporter reporter) throws IOException {

		float embarkedMales = 0;
		float embarkedFemales = 0;
		float survivedFemales = 0; 
		float survivedMales = 0;

		IntWritable passengersClass = pclass;


		while (values.hasNext()) {

			String[] passenger = Text.decode(values.next().copyBytes()).split(",");
			
			if (passenger[0].equals("male")){
				embarkedMales += 1;
				survivedMales += passenger[1].equals("survived") ? 1 : 0;
			}
			else if (passenger[0].equals("female")){
				embarkedFemales +=1;
				survivedFemales += passenger[1].equals("survived") ? 1 : 0;
			}
			
		}

		survivedMales = 100 * survivedMales / (embarkedMales == 0.0 ? 1 : embarkedMales); // avoid division by 0
		survivedFemales = 100 * survivedFemales / (embarkedFemales == 0.0 ? 1 : embarkedFemales);
		
		String result = Float.toString(survivedMales) + ", " + Float.toString(survivedFemales);

		output.collect(passengersClass, new Text(result));
	}
}
