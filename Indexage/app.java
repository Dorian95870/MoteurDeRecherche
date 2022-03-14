public class app {

	public static void main(String[] args) {
		JsonExplorer explorer = new JsonExplorer("./dataset2.json");
		//System.out.println(explorer.getFromIndex(220));
		System.out.println(explorer.getFromIndex(70L).get("title"));
		
		//System.out.println(explorer.getFromCateg("title"));
		
		System.out.println(Indexer.start(explorer.getFromCateg("title")));
		
	}
}
