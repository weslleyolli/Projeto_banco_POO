package aula_02;

import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

public class WebScrapping {

	public static void main(String[] args) throws IOException{
		Document doc = Jsoup.connect("https://pt.wikipedia.org/wiki/Campinense_Clube").get();
		
		System.out.println(doc.getElementsContainingOwnText("Copa do Nordeste 2013"));

	}
}
