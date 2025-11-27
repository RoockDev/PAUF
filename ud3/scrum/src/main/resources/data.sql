-- 1. Aseguramos un Estado de Tarea y una Prioridad (para que no falle la tarea)
-- Usamos la tabla 'estado_entity' y 'prioridad_entity' de tu foto
INSERT INTO estado_entity (id, nombre) VALUES (1, 'TODO') ON CONFLICT (id) DO NOTHING;
INSERT INTO prioridad_entity (id, nombre) VALUES (1, 'MEDIA') ON CONFLICT (id) DO NOTHING;

-- 2. Insertamos el SPRINT 1
-- Usamos la tabla 'sprints' (la del plural, que coincide con tu clase Java)
-- Asumimos que el estado_sprint con ID 1 ('PLANNED') ya existe de antes
INSERT INTO sprints (id, nombre, fecha_inicio, fecha_fin, objetivo, estado_id)
VALUES (1, 'Sprint Examen', '2025-11-01', '2025-11-15', 'Objetivo Aprobar', 1)
    ON CONFLICT (id) DO NOTHING;

-- 3. Insertamos las 3 TAREAS vinculadas al Sprint 1
-- Tabla 'tarea' (singular, como en tu foto)
-- sprint_id = 1 (El que acabamos de crear)
-- programador_id = 1 (El que ya tienes creado)
INSERT INTO tarea (titulo, descripcion, story_points, estimacion_horas, horas_invertidas, fecha_creacion, fecha_actualizacion, prioridad_id, estado_id, programador_id, sprint_id)
VALUES
    ('Tarea Sergio 1', 'Primera tarea', 5, 8, 0, CURRENT_DATE, CURRENT_DATE, 1, 1, 1, 1),
    ('Tarea Zarcero 2', 'Segunda tarea', 3, 4, 0, CURRENT_DATE, CURRENT_DATE, 1, 1, 1, 1),
    ('Tarea Pérez 3', 'Tercera tarea', 8, 16, 0, CURRENT_DATE, CURRENT_DATE, 1, 1, 1, 1);