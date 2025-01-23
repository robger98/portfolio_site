import { projects } from "./projects"

export function load() {
    return { projects: projects.map(p => ({name: p.name, description: p.description, link: p.link})) }
}