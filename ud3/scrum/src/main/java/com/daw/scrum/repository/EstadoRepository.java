package com.daw.scrum.repository;

import com.daw.scrum.model.EstadoEntity;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface EstadoRepository extends JpaRepository<EstadoEntity, Long> {

    Optional<EstadoEntity> findByNombre(String nombre);

}

