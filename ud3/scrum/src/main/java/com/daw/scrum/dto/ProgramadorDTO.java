package com.daw.scrum.dto;

import com.daw.scrum.model.Rol;

public class ProgramadorDTO {
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Rol getRol() {
        return rol;
    }

    public void setRol(Rol rol) {
        this.rol = rol;
    }

    public Integer getCapacidadHoras() {
        return capacidadHoras;
    }

    public void setCapacidadHoras(Integer capacidadHoras) {
        this.capacidadHoras = capacidadHoras;
    }

    private Long id;
    private String nombre;
    private String email;
    private Rol rol;
    private Integer capacidadHoras;

}
