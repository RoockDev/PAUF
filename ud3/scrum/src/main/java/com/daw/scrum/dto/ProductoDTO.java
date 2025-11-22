package com.daw.scrum.dto;

import com.daw.scrum.model.TipoProducto;
import jakarta.persistence.*;

public class ProductoDTO {


    private Long id;

    private String nombre;

    private double precio;

    private TipoProducto tipoProducto;



    public ProductoDTO(Long id, String nombre, double precio, TipoProducto tipoProducto) {
        this.id = id;
        this.nombre = nombre;
        this.precio = precio;
        this.tipoProducto = tipoProducto;
    }

    public ProductoDTO(){}

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

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public TipoProducto getTipoProducto() {
        return tipoProducto;
    }

    public void setTipoProducto(TipoProducto tipoProducto) {
        this.tipoProducto = tipoProducto;
    }

}
