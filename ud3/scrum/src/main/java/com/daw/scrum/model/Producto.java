package com.daw.scrum.model;

import jakarta.persistence.*;

@Entity
public class Producto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false,unique = true)
    private String nombre;

    private double precio;

    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "tipo_producto_id", referencedColumnName = "id", unique = true)
    private TipoProducto tipoProducto;



    public Producto(Long id, String nombre, double precio, TipoProducto tipoProducto) {
        this.id = id;
        this.nombre = nombre;
        this.precio = precio;
        this.tipoProducto = tipoProducto;
    }

    public Producto( String nombre, double precio, TipoProducto tipoProducto) {

        this.nombre = nombre;
        this.precio = precio;
        this.tipoProducto = tipoProducto;
    }

    public Producto(){}

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
