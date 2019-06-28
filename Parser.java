import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.net.URL;

//import org.jsoup.select.Elements;

public class Parser {

    private static Document getPage() throws IOException {
        String url = "https://weather.com/ru-RU/weather/tenday/l/UPXX0016:1:UP";
        Document page = Jsoup.parse(new URL(url), 3000);
        return page;
    }

    private static void printForValues (Elements values, int index){
        for (int i = 0; i < 1; i++){
            Element valueLine = values.get(index);
            for (Element td : valueLine.select("td")){
                System.out.print(td.text() + "        ");
            }
            System.out.println();
        }
    }

    public static void main(String[]args)throws IOException{
        Document page = getPage();
        // css query language
        Element tableWth = page.select("table[classname=twc-table]").first();
        // System.out.println(tableWth);
        Elements names = tableWth.select("tr[classname=clickable closed]");
        int index = 0;

        for (Element name : names){
            String Date = name.select("span[class=day-detail clearfix]").text();
            System.out.println("        " + Date + "               Описание               Макс/Мин        Осадки       Ветер          Влажность");
            printForValues(names, index);
            index++;
        }

    }
}
