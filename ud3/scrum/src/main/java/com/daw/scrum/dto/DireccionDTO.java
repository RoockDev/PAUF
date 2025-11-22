package com.daw.scrum.dto;

public class DireccionDTO {
    private Long Id;

    private String calle;

    private String numero;

    private String localidad;

    public DireccionDTO(Long id, String calle, String numero, String localidad) {
        Id = id;
        this.calle = calle;
        this.numero = numero;
        this.localidad = localidad;
    }

    public Long getId() {
        return Id;
    }

    public void setId(Long id) {
        Id = id;
    }

    public String getCalle() {
        return calle;
    }

    public void setCalle(String calle) {
        this.calle = calle;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public String getLocalidad() {
        return localidad;
    }

    public void setLocalidad(String localidad) {
        this.localidad = localidad;
    }
}
