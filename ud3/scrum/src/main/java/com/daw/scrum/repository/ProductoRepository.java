package com.daw.scrum.repository;

import com.daw.scrum.model.Producto;
import com.daw.scrum.model.Usuario;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductoRepository extends JpaRepository<Producto, Long> {

}
