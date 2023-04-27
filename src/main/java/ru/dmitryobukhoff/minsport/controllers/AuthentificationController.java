package ru.dmitryobukhoff.minsport.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller()
@RequestMapping("/auth")
public class AuthentificationController {
    @GetMapping()
    public String authentificationPage(Model model){
        //model.addAttribute("user", new User());
        return "auth/registration";
    }

    @GetMapping("/exit")
    public String exitPage(){
        return "auth/exit";
    }
}
