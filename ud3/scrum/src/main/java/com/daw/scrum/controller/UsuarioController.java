package com.daw.scrum.controller;
import com.daw.scrum.dto.UsuarioDTO;
import com.daw.scrum.service.UsuarioService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class UsuarioController {

    @Autowired
    private UsuarioService usuarioService;

    @GetMapping("/api/listaUsuarios")
    public List<UsuarioDTO> listar() {
        return usuarioService.obtenerUsuarios();
    }

    @GetMapping("/api/listarPorEmail/{email}")
    public List<UsuarioDTO> listarPorEmail(@PathVariable("email") String email) {
        System.out.println(email);
        return usuarioService.obtenerUsuariosPorEmail(email);
    }

    @PostMapping("api/crearUsuario")
    public UsuarioDTO crearUsuario(@RequestBody UsuarioDTO usuarioDTO){
        return usuarioService.crearUsuario(usuarioDTO);
    }

    @GetMapping("api/obtenerUsuario/{id}")
    public UsuarioDTO obtenerUsuario(@PathVariable("id") Long id){
        return usuarioService.obtenerUsuario(id);
    }


}

