package com.unifacisa;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.StringWriter;
import java.util.ArrayList;
import java.util.List;

import com.fasterxml.jackson.core.JsonGenerationException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class App 
{
	public static void main( String[] args ) throws JsonGenerationException, JsonMappingException, IOException {
        ObjectMapper mapper = new ObjectMapper();

        // Serialize with formatting (pretty print)
        StringWriter writer = new StringWriter();
        mapper.writerWithDefaultPrettyPrinter().writeValue(writer, getPessoas());
        System.out.println(writer);

        // Serialize to file
        File file = new File("pessoas.json");
        FileWriter fw = new FileWriter(file);
        mapper.writerWithDefaultPrettyPrinter().writeValue(fw, getPessoas());
        fw.close();

        // Deserialize
        String jsonInput = "[{\"id\":1,\"nome\":\"Lucas\"},{\"id\":2,\"nome\":\"Maria\"},{\"id\":3,\"nome\":\"Jose\"}]";
        List<Pessoa> p = mapper.readValue(jsonInput, new TypeReference<List<Pessoa>>(){});
        System.out.println("Pessoa: " + p);

    }
    private static List<Pessoa> getPessoas() {

        List<Pessoa> pessoas = new ArrayList<Pessoa>();

        Pessoa p1 = new Pessoa();
        p1.setId(1);
        p1.setNome("Lucas");
        p1.setIdade(21);
        p1.setNacionalidade("brasileiro");
        p1.setSexo("masculino");

        Pessoa p2 = new Pessoa();
        p2.setId(2);
        p2.setNome("Maria");
        p2.setIdade(23);
        p2.setNacionalidade("turquistanesa");
        p2.setSexo("feminino");

        Pessoa p3 = new Pessoa();
        p3.setId(3);
        p3.setNome("Jose");
        p3.setIdade(69);
        p3.setNacionalidade("israelita");
        p3.setSexo("masculino");

        pessoas.add(p1);
        pessoas.add(p2);
        pessoas.add(p3);

        return pessoas;

    }
}