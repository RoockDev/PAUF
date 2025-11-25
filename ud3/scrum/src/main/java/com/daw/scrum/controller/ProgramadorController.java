package com.daw.scrum.controller;

import com.daw.scrum.dto.ProgramadorDTO;
import com.daw.scrum.model.Programador;
import com.daw.scrum.repository.ProgramadorRepository;
import com.daw.scrum.service.ProgramadorService;
import com.daw.scrum.model.Rol;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.List;

@RestController
@RequestMapping("/api/programadores")
public class ProgramadorController {

    private final ProgramadorService programadorService;
    private final ProgramadorRepository programadorRepository;

    public ProgramadorController(ProgramadorService programadorService, ProgramadorRepository programadorRepository) {
        this.programadorService = programadorService;
        this.programadorRepository = programadorRepository;
    }

    @GetMapping
    public List<ProgramadorDTO> buscarPorNombre(@RequestParam String nombre){
        return  programadorService.buscarPorNombre(nombre);
    }

    @PostMapping
    public ProgramadorDTO crearProgramador(@RequestBody ProgramadorDTO dto){
        return programadorService.crearProgramador(dto);
    }

    @GetMapping("/rol/{rol}")
    public List<ProgramadorDTO> buscarPorRol(@PathVariable Rol rol) {
        return programadorService.buscarPorRol(rol);
    }

    @GetMapping("/{id}")
    public ProgramadorDTO buscarPorId(@PathVariable Long id) {
        return programadorService.buscarPorId(id);
    }




}
