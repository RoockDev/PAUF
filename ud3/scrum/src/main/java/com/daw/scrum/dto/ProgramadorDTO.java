package com.daw.scrum.dto;

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


    public Integer getCapacidadHoras() {
        return capacidadHoras;
    }

    public void setCapacidadHoras(Integer capacidadHoras) {
        this.capacidadHoras = capacidadHoras;
    }

    private Long id;
    private String nombre;
    private String email;

    public Long getRolId() {
        return rolId;
    }

    public void setRolId(Long rolId) {
        this.rolId = rolId;
    }

    private Long rolId;

    private Integer capacidadHoras;

}
