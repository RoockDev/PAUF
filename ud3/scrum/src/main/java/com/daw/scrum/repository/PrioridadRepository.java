package com.daw.scrum.repository;
import com.daw.scrum.model.PrioridadEntity;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface PrioridadRepository extends JpaRepository<PrioridadEntity,Long>{
    Optional<PrioridadEntity> findByNombre(String nombre);

}
