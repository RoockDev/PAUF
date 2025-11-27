package com.daw.scrum.model;
import jakarta.persistence.*;
import java.time.LocalDateTime;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.JoinColumn;
import com.daw.scrum.model.PrioridadEntity;
import com.daw.scrum.model.EstadoEntity;
import java.util.List;
import java.util.ArrayList;




@Entity
public class Tarea {

   @Id
   @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

 public String getTitulo() {
  return titulo;
 }

 public void setTitulo(String titulo) {
  this.titulo = titulo;
 }

 public Long getId() {
  return id;
 }

 public void setId(Long id) {
  this.id = id;
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

 public Programador getProgramador() {
  return programador;
 }

 public void setProgramador(Programador programador) {
  this.programador = programador;
 }

 private String titulo;
    private String descripcion;
    private Integer storyPoints;

 public PrioridadEntity getPrioridad() {
  return prioridad;
 }

 public void setPrioridad(PrioridadEntity prioridad) {
  this.prioridad = prioridad;
 }

 @ManyToOne
   @JoinColumn(name = "prioridad_id", nullable = false)
   private PrioridadEntity prioridad;

 public EstadoEntity getEstado() {
  return estado;
 }

 public void setEstado(EstadoEntity estado) {
  this.estado = estado;
 }

 @ManyToOne
 @JoinColumn(name = "estado_id", nullable = false)
 private EstadoEntity estado;

 public Sprint getSprint() {
  return sprint;
 }

 public void setSprint(Sprint sprint) {
  this.sprint = sprint;
 }

 @ManyToOne
 @JoinColumn(name = "sprint_id")
 private Sprint sprint;


 private Integer estimacionHoras;
    private Integer horasInvertidas;

    private LocalDateTime fechaCreacion;
    private LocalDateTime fechaActualizacion;

    @ManyToOne
    @JoinColumn(name = "programador_id", nullable = false)
    private Programador programador;


 // RELACIÓN MUCHOS A MUCHOS
 @ManyToMany
 @JoinTable(
         name = "tarea_etiquetas",                  // Nombre de la tabla intermedia que se creará sola
         joinColumns = @JoinColumn(name = "tarea_id"),
         inverseJoinColumns = @JoinColumn(name = "etiqueta_id")
 )
 private List<EtiquetaEntity> etiquetas = new ArrayList<>();


 public List<EtiquetaEntity> getEtiquetas() {
  return etiquetas;
 }

 public void setEtiquetas(List<EtiquetaEntity> etiquetas) {
  this.etiquetas = etiquetas;
 }
}
