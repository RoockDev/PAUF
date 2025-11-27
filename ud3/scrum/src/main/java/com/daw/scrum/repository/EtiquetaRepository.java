package com.daw.scrum.repository;

import com.daw.scrum.model.EtiquetaEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EtiquetaRepository extends JpaRepository<EtiquetaEntity, Long> {
}