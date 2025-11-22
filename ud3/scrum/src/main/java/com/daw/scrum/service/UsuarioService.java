package com.daw.scrum.service;

import com.daw.scrum.dto.UsuarioDTO;
import com.daw.scrum.model.Usuario;
import com.daw.scrum.repository.UsuarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UsuarioService {

    @Autowired
    private UsuarioRepository usuarioRepository;

    public List<UsuarioDTO> obtenerUsuarios() {
        return usuarioRepository.findAll()
                .stream()
                .map(u -> new UsuarioDTO(u.getId(), u.getNombre(), u.getEmail(), u.getDireccion()))
                .toList();
    }

    public List<UsuarioDTO> obtenerUsuariosPorEmail(String email) {
            return usuarioRepository.findByEmail(email).stream().
                    map(u -> new UsuarioDTO(u.getId(), u.getNombre(), u.getEmail(), u.getDireccion())).toList();
    }

    public UsuarioDTO crearUsuario(UsuarioDTO usuarioDTO) {
        Usuario usuario = new Usuario(null,usuarioDTO.getNombre(),usuarioDTO.getEmail(),null,usuarioDTO.getDireccion());
        usuario = usuarioRepository.save(usuario);
        return new UsuarioDTO(
                usuario.getId(),
                usuario.getNombre(),
                usuario.getEmail(),
                usuario.getDireccion()
        );

    }

    public UsuarioDTO obtenerUsuario(Long id) {
         Usuario usuario = usuarioRepository.findById(id).orElse(null);
         if (usuario == null) {
             return null;
         } else {
             return new UsuarioDTO(usuario.getId(),usuario.getNombre(), usuario.getEmail(), usuario.getDireccion());
         }

    }
}
