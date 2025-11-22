package com.daw.scrum.controller;

import com.daw.scrum.dto.TareaDTO;
import com.daw.scrum.service.TareaService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/tareas")
public class TareaController {

    private final TareaService tareaService;

    public TareaController(TareaService tareaService) {
        this.tareaService = tareaService;
    }

    @PostMapping
    public TareaDTO crearTarea(@RequestBody TareaDTO dto) {
        return tareaService.crearTarea(dto);
    }

    @GetMapping("/{id}")
    public TareaDTO buscarPorId(@PathVariable Long id) {
        return tareaService.buscarPorId(id);
    }

    @GetMapping
    public List<TareaDTO> listarTodas() {
        return tareaService.listarTodas();
    }

}
