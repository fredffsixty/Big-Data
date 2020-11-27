package survivedpassengers;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;

public class SurvivedPassengersDriver {
    public static void main(String[] args) {

        // Create a configuration object for the job
        JobConf conf = new JobConf(SurvivedPassengersDriver.class);

        // Set a name of the Job
        conf.setJobName("SurvivedPerClass");

        // Specify data type of output key and value
        conf.setOutputKeyClass(IntWritable.class);
        conf.setOutputValueClass(ArrayWritable.class);

        // Specify data type for mapper output key and value
        conf.setMapOutputKeyClass(IntWritable.class);
        conf.setMapOutputValueClass(Text.class);
        
        // Specify names of Mapper and Reducer Class
        conf.setMapperClass(survivedpassengers.SurvivedPassengersMap.class);
        conf.setReducerClass(survivedpassengers.SurvivedPassengersReduce.class);

        // Specify formats of the data type of Input and output
        conf.setInputFormat(TextInputFormat.class);
        conf.setOutputFormat(TextOutputFormat.class);

        // Set input and output directories using command line arguments, 
        //arg[0] = name of input directory on HDFS, 
        // and arg[1] =  name of output directory to be created to store the output file.

        FileInputFormat.setInputPaths(conf, new Path(args[0]));
        FileOutputFormat.setOutputPath(conf, new Path(args[1]));

        try {
            // Run the job 
            JobClient.runJob(conf);
        } catch (Exception e) {
            e.printStackTrace();
        }    
    }
}
