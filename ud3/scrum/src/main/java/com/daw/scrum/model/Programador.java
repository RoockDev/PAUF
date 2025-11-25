package com.daw.scrum.model;
import com.daw.scrum.model.RolEntity;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.JoinColumn;


import jakarta.persistence.*;

@Entity
public class Programador {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nombre;

    private String email;

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

    public RolEntity getRol() {
        return rol;
    }

    public void setRol(RolEntity rol) {
        this.rol = rol;
    }

    @ManyToOne
    @JoinColumn(name = "rol_id", nullable = false)
    private RolEntity rol;


    private Integer capacidadHoras;

}
