package com.daw.scrum.repository;
import java.util.List;
import com.daw.scrum.model.Programador;
import com.daw.scrum.model.Rol;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProgramadorRepository extends JpaRepository<Programador, Long> {
  List<Programador> findByNombreContainingIgnoreCase(String nombre);
  List<Programador> findByRol(Rol rol);





}
