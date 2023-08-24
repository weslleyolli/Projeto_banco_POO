package aula_02;

import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import org.jsoup.Jsoup;

public class Atividade02 {
    public static void main(String[] args) throws IOException {
        Document doc = Jsoup.connect("https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht").get();

        Elements LeituraGeral = doc.select("ul.ipc-metadata-list");

        try (BufferedWriter writer = new BufferedWriter(new FileWriter("filmes.txt"))) {
            for (Element e : LeituraGeral.select("li.ipc-metadata-list-summary-item")) {
                String nomeFilme = e.select("h3.ipc-title__text").text();
                String informacoesFilme = e.select("li.sc-ee64acb1-1 span").text();

                writer.write(nomeFilme);
                writer.newLine();
                writer.write(informacoesFilme);
                writer.newLine();
                writer.newLine(); 
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}