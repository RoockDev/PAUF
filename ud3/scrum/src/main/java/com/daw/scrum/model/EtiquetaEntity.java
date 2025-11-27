package com.daw.scrum.model;

import jakarta.persistence.*;

@Entity
@Table(name = "etiquetas")
public class EtiquetaEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String nombre; // Ej: "backend", "bug", "ux"

    // Constructores
    public EtiquetaEntity() {
    }

    public EtiquetaEntity(String nombre) {
        this.nombre = nombre;
    }

    // Getters y Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
}