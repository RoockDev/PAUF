package com.daw.scrum.service;
import com.daw.scrum.model.Programador;
import com.daw.scrum.dto.ProgramadorDTO;
import com.daw.scrum.model.RolEntity;
import com.daw.scrum.repository.RolRepository;


import com.daw.scrum.repository.ProgramadorRepository;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.ArrayList;

@Service
public class ProgramadorService {

    private final ProgramadorRepository programadorRepository;
    private final RolRepository rolRepository;


    public ProgramadorService(ProgramadorRepository programadorRepository,
                              RolRepository rolRepository) {
        this.programadorRepository = programadorRepository;
        this.rolRepository = rolRepository;
    }


    private ProgramadorDTO toDTO(Programador programador) {
        if (programador == null) {
            return null;
        }

        ProgramadorDTO dto = new ProgramadorDTO();
        dto.setId(programador.getId());
        dto.setNombre(programador.getNombre());
        dto.setEmail(programador.getEmail());
        dto.setCapacidadHoras(programador.getCapacidadHoras());


        if (programador.getRol() != null) {
            dto.setRolId(programador.getRol().getId());
        }

        return dto;
    }


    private Programador toEntity(ProgramadorDTO dto) {
        if (dto == null) {
            return null;
        }

        Programador programador = new Programador();
        programador.setId(dto.getId());
        programador.setNombre(dto.getNombre());
        programador.setEmail(dto.getEmail());
        programador.setCapacidadHoras(dto.getCapacidadHoras());

        // ROL (nuevo)
        if (dto.getRolId() != null) {
            rolRepository.findById(dto.getRolId())
                    .ifPresent(programador::setRol);
        }

        return programador;
    }


    public List<ProgramadorDTO> buscarPorNombre(String nombre){
        List<Programador> programadores = programadorRepository.findByNombreContainingIgnoreCase(nombre);

        List<ProgramadorDTO> resultado = new ArrayList<>();

        for (Programador p : programadores){
            resultado.add(toDTO(p));
        }

        return resultado;
    }

    public ProgramadorDTO crearProgramador(ProgramadorDTO dto){
        //DTO -> entidad
        Programador programador = toEntity(dto);

        //Se guarda en bbdd
        Programador guardado = programadorRepository.save(programador);

        //Entidad guardada -> DTO de respuesta
        return toDTO(guardado);

    }

    public List<ProgramadorDTO> buscarPorRol(Long rolId){
        // Buscar el rol en la base de datos
        RolEntity rol = rolRepository.findById(rolId).orElse(null);

        if (rol == null){
            return new ArrayList<>();
        }

        List<Programador> programadores = programadorRepository.findByRol(rol);

        List<ProgramadorDTO> resultado = new ArrayList<>();
        for (Programador p: programadores){
            resultado.add(toDTO(p));
        }

        return resultado;
    }

    public ProgramadorDTO buscarPorId(Long id) {
        return programadorRepository.findById(id)
                .map(this::toDTO)        // si lo encuentra, lo convierte a DTO
                .orElse(null);           // si no, devuelve null
    }


}
