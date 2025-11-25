package com.daw.scrum.dto;

import com.daw.scrum.model.Prioridad;
import com.daw.scrum.model.Estado;
import com.daw.scrum.model.PrioridadEntity;

import java.time.LocalDateTime;

public class TareaDTO {

    private String titulo;
    private String descripcion;
    private Integer storyPoints;

    public PrioridadEntity getPrioridad() {
        return prioridad;
    }

    public void setPrioridad(PrioridadEntity prioridad) {
        this.prioridad = prioridad;
    }

    private PrioridadEntity prioridad;

    public Long getEstadoId() {
        return estadoId;
    }

    public void setEstadoId(Long estadoId) {
        this.estadoId = estadoId;
    }

    private Long estadoId;

    private Integer estimacionHoras;
    private Integer horasInvertidas;
    private LocalDateTime fechaCreacion;
    private LocalDateTime fechaActualizacion;
    private Long programadorId;
    private Long id;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public Integer getStoryPoints() {
        return storyPoints;
    }

    public void setStoryPoints(Integer storyPoints) {
        this.storyPoints = storyPoints;
    }





    public Integer getEstimacionHoras() {
        return estimacionHoras;
    }

    public void setEstimacionHoras(Integer estimacionHoras) {
        this.estimacionHoras = estimacionHoras;
    }

    public Integer getHorasInvertidas() {
        return horasInvertidas;
    }

    public void setHorasInvertidas(Integer horasInvertidas) {
        this.horasInvertidas = horasInvertidas;
    }

    public LocalDateTime getFechaCreacion() {
        return fechaCreacion;
    }

    public void setFechaCreacion(LocalDateTime fechaCreacion) {
        this.fechaCreacion = fechaCreacion;
    }

    public LocalDateTime getFechaActualizacion() {
        return fechaActualizacion;
    }

    public void setFechaActualizacion(LocalDateTime fechaActualizacion) {
        this.fechaActualizacion = fechaActualizacion;
    }

    public Long getProgramadorId() {
        return programadorId;
    }

    public void setProgramadorId(Long programadorId) {
        this.programadorId = programadorId;
    }


}
