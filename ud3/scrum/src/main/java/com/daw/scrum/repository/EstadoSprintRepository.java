package com.daw.scrum.repository;

import com.daw.scrum.model.EstadoSprint;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.Optional;

@Repository
public interface EstadoSprintRepository extends JpaRepository<EstadoSprint, Long> {

    Optional<EstadoSprint> findByNombre(String nombre);

}
