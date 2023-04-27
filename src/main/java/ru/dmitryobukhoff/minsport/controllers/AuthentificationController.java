package ru.dmitryobukhoff.minsport.controllers;

import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import ru.dmitryobukhoff.minsport.models.UsersEntity;

@Controller()
@RequestMapping("/auth")
public class AuthentificationController {
//    @Autowired
//    @Qualifier(value = "UserDAO")
//    private UserDAO userDAO;

    @GetMapping()
    public String authentificationPage(Model model){
        model.addAttribute("person", new UsersEntity());
        return "auth/registration";
    }

    @GetMapping("/exit")
    public String exitPage(){
        return "auth/exit";
    }

    @PostMapping()
    public String create(@ModelAttribute("person") @Valid UsersEntity user,
                         BindingResult bindingResult){
        if(!bindingResult.hasErrors()){
            return "auth/registration";
        }
        //сохранение в БД
        return "redirect:/sport";


    }
}
