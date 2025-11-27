package com.daw.scrum.dto;


import java.time.LocalDateTime;
import java.util.List;

public class TareaDTO {

    private Long id;
    private String titulo;
    private String descripcion;
    private Integer storyPoints;

    private Long prioridadId;
    private Long estadoId;
    private Long programadorId;

    private Integer estimacionHoras;
    private Integer horasInvertidas;
    private LocalDateTime fechaCreacion;
    private LocalDateTime fechaActualizacion;


    private Long sprintId;

    public List<Long> getEtiquetaIds() {
        return etiquetaIds;
    }

    public void setEtiquetaIds(List<Long> etiquetaIds) {
        this.etiquetaIds = etiquetaIds;
    }

    private List<Long> etiquetaIds;

    public Long getSprintId() {
        return sprintId;
    }

    public void setSprintId(Long sprintId) {
        this.sprintId = sprintId;
    }

    // GETTERS y SETTERS

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

    public Long getPrioridadId() {
        return prioridadId;
    }

    public void setPrioridadId(Long prioridadId) {
        this.prioridadId = prioridadId;
    }

    public Long getEstadoId() {
        return estadoId;
    }

    public void setEstadoId(Long estadoId) {
        this.estadoId = estadoId;
    }

    public Long getProgramadorId() {
        return programadorId;
    }

    public void setProgramadorId(Long programadorId) {
        this.programadorId = programadorId;
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
}
