package com.daw.scrum.repository;


import com.daw.scrum.model.Sprint;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SprintRepository extends JpaRepository<Sprint, Long> {
    // De momento lo dejamos vacío.
    // JpaRepository ya nos regala: save(), findAll(), findById(), delete()...
}
