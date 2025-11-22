package com.daw.scrum.dto;

import com.daw.scrum.model.Direccion;

public class UsuarioDTO {
    private Long id;
    private String nombre;
    private String email;
    private Direccion direccion;


    public UsuarioDTO(Long id, String nombre, String email, Direccion direccion) {
        this.id = id;
        this.nombre = nombre;
        this.email = email;
        this.direccion = direccion;
    }

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

    public Direccion getDireccion() {
        return direccion;
    }

    public void setDireccion(Direccion direccion) {
        this.direccion = direccion;
    }
}
