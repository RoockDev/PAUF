package com.daw.scrum.service;
import com.daw.scrum.model.Tarea;
import com.daw.scrum.model.Programador;
import com.daw.scrum.dto.TareaDTO;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import com.daw.scrum.repository.TareaRepository;
import com.daw.scrum.repository.ProgramadorRepository;
import org.springframework.stereotype.Service;

@Service
public class TareaService {

    private final TareaRepository tareaRepository;
    private final ProgramadorRepository programadorRepository;

    public TareaService(TareaRepository tareaRepository, ProgramadorRepository programadorRepository) {
        this.tareaRepository = tareaRepository;
        this.programadorRepository = programadorRepository;
    }


    private TareaDTO toDTO(Tarea tarea) {
        if (tarea == null) {
            return null;
        }

        TareaDTO dto = new TareaDTO();
        dto.setId(tarea.getId());
        dto.setTitulo(tarea.getTitulo());
        dto.setDescripcion(tarea.getDescripcion());
        dto.setStoryPoints(tarea.getStoryPoints());
        dto.setPrioridad(tarea.getPrioridad());
        dto.setEstado(tarea.getEstado());
        dto.setEstimacionHoras(tarea.getEstimacionHoras());
        dto.setHorasInvertidas(tarea.getHorasInvertidas());
        dto.setFechaCreacion(tarea.getFechaCreacion());
        dto.setFechaActualizacion(tarea.getFechaActualizacion());

        // programadorId viene de la entidad Programador
        if (tarea.getProgramador() != null) {
            dto.setProgramadorId(tarea.getProgramador().getId());
        }

        return dto;
    }



    private Tarea toEntity(TareaDTO dto) {
        if (dto == null) {
            return null;
        }

        Tarea tarea = new Tarea();
        tarea.setId(dto.getId());
        tarea.setTitulo(dto.getTitulo());
        tarea.setDescripcion(dto.getDescripcion());
        tarea.setStoryPoints(dto.getStoryPoints());
        tarea.setPrioridad(dto.getPrioridad());
        tarea.setEstado(dto.getEstado());
        tarea.setEstimacionHoras(dto.getEstimacionHoras());
        tarea.setHorasInvertidas(dto.getHorasInvertidas());
        tarea.setFechaCreacion(dto.getFechaCreacion());
        tarea.setFechaActualizacion(dto.getFechaActualizacion());

        if (dto.getProgramadorId() != null) {
            Optional<Programador> programadorOpt = programadorRepository.findById(dto.getProgramadorId());
            programadorOpt.ifPresent(tarea::setProgramador);
            // si no existe, podríamos lanzar excepción, pero de momento lo dejamos así
        }

        return tarea;
    }

    public TareaDTO crearTarea(TareaDTO dto) {
        // DTO -> entidad
        Tarea tarea = toEntity(dto);

        // ignoramos las fechas  que vengan en el DTO
        tarea.setFechaCreacion(LocalDateTime.now());
        tarea.setFechaActualizacion(LocalDateTime.now());

        // se guarda en bbdd
        Tarea guardada = tareaRepository.save(tarea);

        // Entidad -> DTO de respuesta
        return toDTO(guardada);
    }

    public TareaDTO buscarPorId(Long id) {
        return tareaRepository.findById(id)
                .map(this::toDTO)
                .orElse(null);
    }

    public List<TareaDTO> listarTodas(){
        List<Tarea> tareas = tareaRepository.findAll();
        List<TareaDTO> resultado = new ArrayList<>();
        for (Tarea t: tareas){
            resultado.add(toDTO(t));
        }

        return resultado;
    }









}
