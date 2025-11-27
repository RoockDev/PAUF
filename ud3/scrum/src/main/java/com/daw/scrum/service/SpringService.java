package com.daw.scrum.service;

import com.daw.scrum.dto.SprintDTO;
import com.daw.scrum.model.EstadoSprint;
import com.daw.scrum.model.Sprint;
import com.daw.scrum.repository.EstadoSprintRepository;
import com.daw.scrum.repository.SprintRepository;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class SpringService {

    private final SprintRepository sprintRepository;
    private final EstadoSprintRepository estadoSprintRepository;

    public SpringService(SprintRepository sprintRepository, EstadoSprintRepository estadoSprintRepository) {
        this.sprintRepository = sprintRepository;
        this.estadoSprintRepository = estadoSprintRepository;
    }

    private SprintDTO toDTO(Sprint sprint) {
        if (sprint == null) {
            return null;
        }

        SprintDTO dto = new SprintDTO();
        dto.setId(sprint.getId());
        dto.setNombre(sprint.getNombre());
        dto.setFechaInicio(sprint.getFechaInicio());
        dto.setFechaFin(sprint.getFechaFin());
        dto.setObjetivo(sprint.getObjetivo());

        // Convertimos la entidad EstadoSprint a String para el DTO
        if (sprint.getEstado() != null) {
            dto.setEstado(sprint.getEstado().getNombre());
        }

        return dto;
    }

    private Sprint toEntity(SprintDTO dto) {
        if (dto == null) {
            return null;
        }

        Sprint sprint = new Sprint();
        sprint.setId(dto.getId());
        sprint.setNombre(dto.getNombre());
        sprint.setFechaInicio(dto.getFechaInicio());
        sprint.setFechaFin(dto.getFechaFin());
        sprint.setObjetivo(dto.getObjetivo());

        // ESTADO (Equivalente a lo que hiciste con ROL)
        // Buscamos el estado por nombre ("PLANNED", "ACTIVE"...)
        if (dto.getEstado() != null) {
            estadoSprintRepository.findByNombre(dto.getEstado())
                    .ifPresent(sprint::setEstado);
        } else {
            // Opcional: Si no envían estado, asignamos PLANNED por defecto
            estadoSprintRepository.findByNombre("PLANNED")
                    .ifPresent(sprint::setEstado);
        }

        return sprint;
    }

}
