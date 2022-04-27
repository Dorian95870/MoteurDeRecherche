package unitTest;
import code.*;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.ArrayList;
import java.util.HashMap;

import org.junit.jupiter.api.Test;

class Indexer_Test {

	@Test
	void test() {
		HashMap<Long, Object> data = new HashMap<Long, Object>();
		data.put(01L, "Il il est");
		data.put(02L, "Il arrete");
		HashMap<String, HashMap<Long, ArrayList<Integer>>> goal = new HashMap<String, HashMap<Long, ArrayList<Integer>>>(){
			private static final long serialVersionUID = 1L;
		{
			put("il", new HashMap<Long, ArrayList<Integer>>(){
				private static final long serialVersionUID = 1L;
			{
				put(01L, new ArrayList<Integer>() {
					private static final long serialVersionUID = 1L;
				{
					add(0);
					add(1);
				}});
				put(02L, new ArrayList<Integer>() {
					private static final long serialVersionUID = 1L;
				{
					add(0);
				}});
			}});
			
			put("arrete", new HashMap<Long, ArrayList<Integer>>(){
				private static final long serialVersionUID = 1L;
			{
				put(02L, new ArrayList<Integer>() {
					private static final long serialVersionUID = 1L;
				{
					add(1);
				}});
			}});
			
			put("est", new HashMap<Long, ArrayList<Integer>>(){
				private static final long serialVersionUID = 1L;
			{
				put(01L, new ArrayList<Integer>() {
					private static final long serialVersionUID = 1L;
				{
					add(2);
				}});
			}});
		}};
		
		HashMap<String, HashMap<Long, ArrayList<Integer>>> res = IndexGen.start(data);
		
		assertEquals(res.toString(), goal.toString());
	}

}
