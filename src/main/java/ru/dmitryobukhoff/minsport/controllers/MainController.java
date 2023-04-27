package ru.dmitryobukhoff.minsport.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/sport")
public class MainController {

    @GetMapping()
    public String mainPage(){
        return "sport/index";
    }

    @GetMapping("/contacts")
    public String contactsPage(){
        return "sport/contacts";
    }

    @GetMapping("/news")
    public String newsPage(){
        return "sport/news";
    }

    @GetMapping("/profile")
    public String profilePage(){
        return "sport/profile";
    }

    @GetMapping("events/event")
    public String eventPage(){
        return "sport/event";
    }

}
