package com.daw.scrum.service;

import com.daw.scrum.dto.TareaDTO;
import com.daw.scrum.model.*;
import com.daw.scrum.repository.*;
import org.springframework.stereotype.Service;
import com.daw.scrum.repository.EtiquetaRepository;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Service
public class TareaService {

    private final TareaRepository tareaRepository;
    private final ProgramadorRepository programadorRepository;
    private final PrioridadRepository prioridadRepository;
    private final EstadoRepository estadoRepository;
    private final SprintRepository sprintRepository;
    private final EtiquetaRepository etiquetaRepository;


    public TareaService(TareaRepository tareaRepository,
                        ProgramadorRepository programadorRepository,
                        PrioridadRepository prioridadRepository,
                        EstadoRepository estadoRepository,
                        SprintRepository sprintRepository, EtiquetaRepository etiquetaRepository) {
        this.tareaRepository = tareaRepository;
        this.programadorRepository = programadorRepository;
        this.prioridadRepository = prioridadRepository;
        this.estadoRepository = estadoRepository;
        this.sprintRepository = sprintRepository;
        this.etiquetaRepository = etiquetaRepository;
    }

    // ───────── Conversión ENTIDAD → DTO ─────────
    private TareaDTO toDTO(Tarea tarea) {
        if (tarea == null) {
            return null;
        }

        TareaDTO dto = new TareaDTO();
        dto.setId(tarea.getId());
        dto.setTitulo(tarea.getTitulo());
        dto.setDescripcion(tarea.getDescripcion());
        dto.setStoryPoints(tarea.getStoryPoints());
        dto.setEstimacionHoras(tarea.getEstimacionHoras());
        dto.setHorasInvertidas(tarea.getHorasInvertidas());
        dto.setFechaCreacion(tarea.getFechaCreacion());
        dto.setFechaActualizacion(tarea.getFechaActualizacion());

        // PRIORIDAD → prioridadId
        if (tarea.getPrioridad() != null) {
            dto.setPrioridadId(tarea.getPrioridad().getId());
        }

        // ESTADO → estadoId
        if (tarea.getEstado() != null) {
            dto.setEstadoId(tarea.getEstado().getId());
        }

        // PROGRAMADOR → programadorId
        if (tarea.getProgramador() != null) {
            dto.setProgramadorId(tarea.getProgramador().getId());
        }

        if (tarea.getSprint() != null){
            dto.setSprintId(tarea.getSprint().getId());
        }

        if (tarea.getEtiquetas() != null) {
            List<Long> ids = new ArrayList<>();
            for (EtiquetaEntity etiq : tarea.getEtiquetas()) {
                ids.add(etiq.getId());
            }
            dto.setEtiquetaIds(ids);
        }



        return dto;
    }

    // ───────── Conversión DTO → ENTIDAD ─────────
    private Tarea toEntity(TareaDTO dto) {
        if (dto == null) return null;

        Tarea tarea = new Tarea();
        tarea.setId(dto.getId());
        tarea.setTitulo(dto.getTitulo());
        tarea.setDescripcion(dto.getDescripcion());
        tarea.setStoryPoints(dto.getStoryPoints());
        tarea.setEstimacionHoras(dto.getEstimacionHoras());
        tarea.setHorasInvertidas(dto.getHorasInvertidas());
        tarea.setFechaCreacion(dto.getFechaCreacion());
        tarea.setFechaActualizacion(dto.getFechaActualizacion());

        // PRIORIDAD (obligatoria en BD)
        if (dto.getPrioridadId() != null) {
            prioridadRepository.findById(dto.getPrioridadId())
                    .ifPresent(tarea::setPrioridad);
        }

        // ESTADO (obligatorio en BD)
        if (dto.getEstadoId() != null) {
            estadoRepository.findById(dto.getEstadoId())
                    .ifPresent(tarea::setEstado);
        }

        // PROGRAMADOR (obligatorio en BD)
        if (dto.getProgramadorId() != null) {
            programadorRepository.findById(dto.getProgramadorId())
                    .ifPresent(tarea::setProgramador);
        }

        if (dto.getSprintId() != null){
            sprintRepository.findById(dto.getSprintId())
                    .ifPresent(tarea::setSprint);
        }

        if (dto.getEtiquetaIds() != null) {
            // findAllById es un método de Spring que busca una lista entera de golpe
            List<EtiquetaEntity> etiquetasEncontradas = etiquetaRepository.findAllById(dto.getEtiquetaIds());
            tarea.setEtiquetas(etiquetasEncontradas);
        }



        return tarea;
    }

    // ───────── CRUD ─────────

    public TareaDTO crearTarea(TareaDTO dto) {
        Tarea tarea = toEntity(dto);

        // ignoramos las fechas que vengan en el DTO
        tarea.setFechaCreacion(LocalDateTime.now());
        tarea.setFechaActualizacion(LocalDateTime.now());

        Tarea guardada = tareaRepository.save(tarea);
        return toDTO(guardada);
    }

    public TareaDTO buscarPorId(Long id) {
        return tareaRepository.findById(id)
                .map(this::toDTO)
                .orElse(null);
    }

    public List<TareaDTO> listarTodas() {
        List<Tarea> tareas = tareaRepository.findAll();
        List<TareaDTO> resultado = new ArrayList<>();
        for (Tarea t : tareas) {
            resultado.add(toDTO(t));
        }
        return resultado;
    }

    //metodo para ejercicio que ha mandao fran
    public List<TareaDTO> buscarPorSprint(Long sprintID){
        //llamamos al repositorio con el nuevo metodo que acabamos de crear
        List<Tarea> tareasEncontradas = tareaRepository.findBySprintId(sprintID);

        //preparamos una lista vacia para guardar los resultados
        List<TareaDTO> resultado = new ArrayList<>();

        //recorremos las tareas encontradas y las convertimos una a una a DTO
        for (Tarea t: tareasEncontradas){
            resultado.add(toDTO(t));
        }

        return resultado;

    }

}
